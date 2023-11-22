function RTBoxFound = checkForRTBox(varargin)

cmd = 'ttl';
nIn=nargin; % # of input
if nIn<1 || ~ischar(varargin{nIn}) || ~strncmpi('device',varargin{nIn},6)
    boxID='device1'; portname=''; % no device specified, use default
else
    boxID=varargin{nIn};
    ind=strfind(boxID,':'); portname='';
    if ~isempty(ind), portname=boxID(ind+1:end); boxID=boxID(1:ind-1); end
    if ~any(boxID=='?'), nIn=nIn-1; end % don't count 'device*'
end
persistent info; % struct containing important device info
persistent eventcodes cmds events4enable tpreOffset infoDft; % only to save time
if isempty(info) % no any opened device
    info=struct('events',{{'1' '2' '3' '4' '1' '2' '3' '4' 'sound' 'light' '5' 'aux' 'serial'}},...
        'enabled',logical([1 0 0 0 0 0]),'ID',boxID,'handle',[],'portname','','sync',[], ...
        'version',[],'clkRatio',1,'TTLWidth',0.00097,'debounceInterval',0.05,...
        'latencyTimer',0.001,'fake',false,'nEventsRead',1,'untilTimeout',false,...
        'TTLresting',logical([0 1]),'clockUnit',1/115200,'cleanObj',[],...
        'MAC',zeros(1,7,'uint8'), 'buffer', 585, 'threshold', 1);
    infoDft=info;
    eventcodes=[49:2:55 50:2:56 97 48 57 98 89]; % code for 13 events
    cmds={'close' 'closeall' 'clear' 'start' 'test' 'buttondown' ...
        'buttonnames' 'enable' 'disable' 'clockratio' 'ttl' 'fake' 'keynames' ...
        'ttlwidth' 'waittr' 'debounceinterval' 'eventsavailable' ...
        'neventsread' 'untiltimeout' 'info' 'ttlresting' 'sound'...
        'enablestate' 'reset' 'purge' 'buffersize' 'threshold'}; % for check only
    events4enable={'press' 'release' 'sound' 'light' 'tr' 'aux'};
    evalc('GetSecs;KbCheck;WaitSecs(0.001);IOPort(''Verbosity'');now;'); % initialize
    tpreOffset=10/115200; % time for 1-byte serial write: 10 bits (1+8+1)
    tpreOffset=tpreOffset+5.5e-6; % time for execution of write cmd (measured shortest)
    % tpreOffset=tpreOffset+1.1e-6; % time for execution of GetSecs in C (measured shortest)
end
id=find(strcmpi(boxID,{info.ID})); % which device?
if isempty(id), id=length(info)+1; info(id)=infoDft; end % add a slot

read=[lower(info(id).events) {'secs' 'boxsecs'}]; % triggers and read commands
if ~any(strcmp(cmd,[cmds read])) % if invalid cmd, we won't open device
    RTBoxError('unknownCmd',in1,cmds,info(id).events); % invalid command
end



    % get possible port list for different OS
    if IsWin
        % suppose you did not assign RTBox to COM1 or 2
        ports = cellstr(num2str((3:256)', '\\\\.\\COM%i'));
        ports = strtrim(ports); % needed for matlab 2009b
    elseif IsOSX
        ports = dir('/dev/cu.usbserialRTBox*');
        macLatFail = 0;
        if isempty(ports)
            ports = dir('/dev/cu.usbserial*'); 
            macLatFail = 1; 
        end
        if ~isempty(ports), ports=strcat('/dev/', {ports.name}); end
    elseif IsLinux
        ports = dir('/dev/ttyUSB*');
        if ~isempty(ports), ports = strcat('/dev/', {ports.name}); end
    else error('Unsupported system: %s.', computer);
    end
    if ~isempty(portname)
        foo = lower(ports);
        ind = strcmpi(portname,foo);
        if ~any(ind)
            foo = strrep(foo, '\\.\','');
            foo = strrep(foo, '/dev/','');
            ind = strcmpi(portname, foo);
        end
        if ~any(ind), RTBoxError('portNotExist', portname); end
        ports = ports(ind); % use the provided port
    end

    nPorts = length(ports);
    if nPorts==0
        fprintf('No serial ports found. Will not use RTBox.\n');
        RTBoxFound = 0;
        return; 
    end
    deviceFound = 0; 
    rec = struct('avail', '', 'busy', ''); % for error record only
    verbo = IOPort('Verbosity', 0); % shut up screen output and error
    cfgStr = 'BaudRate=115200 ReceiveTimeout=1 PollLatency=0';
    for ic = 1:nPorts
        port = ports{ic};
        % this also solves multiple open problem in MAC/Linux
        if any(strcmp(port, {info(1:id-1).portname})), continue; end
        [s, errmsg]=IOPort('OpenSerialPort', port, cfgStr);
        %fprintf 'DEBUG: '; port
        if s>=0  % open succeed
            IOPort('Purge', s); % clear port
            IOPort('Write', s, 'X', 0); % ask identity, switch to advanced mode
            idn = IOPort('Read', s, 1, 21); % contains 'USTCRTBOX'
            if ~IsWin && isempty(strfind(idn, 'USTCRTBOX'))
                IOPort('Close', s); % try to fix ID failure in MAC and Linux
                s = IOPort('OpenSerialPort', port, cfgStr);
                IOPort('Write', s, 'X', 0);
                idn = IOPort('Read', s, 1, 21);
            end
            if length(idn)==1 && idn=='?' % maybe in boot
                IOPort('Write', s, 'R', 0); % return to application
                IOPort('Write', s, 'X', 0);
                idn = IOPort('Read', s, 1, 21);
            end
            if strfind(idn, 'USTCRTBOX'), deviceFound=1; break; end
            rec.avail{end+1} = port; % exist but not RTBox
            IOPort('Close', s); % not RTBox, close it
        elseif isempty(strfind(errmsg, 'ENOENT'))
            rec.busy{end+1} = port; % open failed but port exists
        end
    end
    if ~deviceFound % issue error
        info(id) = [];
        if isempty(portname)
            fprintf('RTBox device not found. Will not use RTBox.\n');
            RTBoxFound = 0;
            return;   
        end
        fprintf('Invalid port. Will not use RTBox.\n');
        RTBoxFound = 0;
        return; 
    else
        RTBoxFound = 1;
        fprintf('RTBox found, will send pulses.\n');
    end
    
    IOPort('Close', s);
end