% % Call the main function to start the task.
% Parameters to enter:
% For fullscreen enter 'full', for small screen enter 'test'
% set which display to use: for current monitor screenNum = 2, for other
% monitor screenNum = 1. For both monitors use screenNum = 0.
% Look up subject ID from SID google drive folder (e.g., '555')
% and specify session condition as abstinent = 'A' or non-abstinent = 'NA'
% also specify run number (2 runs per session)
% finally specify start target duration from either practice or run 1

% eg:
% SID_eeg(1, '555', 'NA', '1', .30)

% NOTE: "other keypress" trigger 15 not sending, but experiment will break
% when you press "q". "Okey" only records the time of the first non-target keypress in each
% trial into the log.

function SID_eeg_final(screenNum, subjectID, sessionCondition, runNumber, startRT)

    KbName('UnifyKeyNames');
    RestrictKeysForKbCheck([]);
    
    %------------------------------------------------------------------------
    %

    %SET UP LOG FILE
    logfiledirectory = ['C:\Users\eegstim\Desktop\SID_Psychopy\m_logfiles']; 
    outputFileName = [logfiledirectory filesep subjectID '-' sessionCondition '-' runNumber '-SID.txt'];

    %------------------------------------------------------------------------
    % CHECK TO AVOID EXISTING FILE
    %------------------------------------------------------------------------
    %If a file with the same name already exists, (i.e. someone has the same
    %initials as another) this provides option to add a character, overwrite, or break
    if exist(outputFileName, 'file')==2
        file_error = input('That file already exists! Append (1), overwrite (2), or break (3/default)?');
        if isempty(file_error)|| file_error ==3
            return;
        elseif file_error==1
            outfile = fopen(outputFileName,'a');
        elseif file_error==2
            outfile = fopen(outputFileName,'w');
        end
    else
        outfile = fopen(outputFileName,'w');
    end
    
    fprintf('Opening logfile: %s\n', outputFileName); 
    fprintf(outfile,'##LOG FOR SUBJECT %s', subjectID);
    fprintf(outfile, '##%s\n', datestr(now));
    fprintf(outfile,'##Start target duration %f\n', startRT);
    fprintf(outfile,'##IncentiveCue\tNeutCue\tTargetOnset\tSKey\tOKey\tThumbsUp\tEqualSign\tITI\n');

    %------------------------------------------------------------------------

    %SET UP DATA FILE
    dataFileDirectory = 'C:\Users\eegstim\Desktop\SID_Psychopy\m_datafiles'; 
        
    % Specify the full path to the CSV file
    fullFilePath = fullfile(dataFileDirectory, sprintf('%s_%s_%s_SID.csv', subjectID, sessionCondition, runNumber));
    

    %------------------------------------------------------------------------


    % Initialize parameters
    % Define timing parameters
    cueDuration = 0.4;
    fixationMinDuration = 2;
    fixationMaxDuration = 2.5;
    targetDurationChange = 0.01;
    fixationAfterTarget = 1.3;
    feedbackDuration = 2;
    ITIduration = 1;
    
    % Create empty lists to store data
    trialNumber = 1:75;
    targetDuration = zeros(1, 75);
    antDuration = zeros(1, 75);
    status = zeros(1, 75);
    RT = zeros(1, 75);
    
    % Load images (remember to update image paths if you move them)
    [incentiveCue, ~, alphaI] = imread('incentivecue.png');
    [neutralCue, ~, alphaN] = imread('neutcue.png');
    [targetImage, ~, alphaT] = imread('target.png');
    [thumbsUpImage, ~, alphaU] = imread('thumbsup.png');
    [equalsImage, ~, alphaE] = imread('equalsign.png');

    % Generate trial types (incentive: 50 trials, neutral: 25 trials)
    trialTypes = [repmat("incentive", 1, 50), repmat("neutral", 1, 25)];
    trialTypes = trialTypes(randperm(length(trialTypes)));
    fprintf('Total number of trials is %d\n', length(trialTypes));
    
    % Initialize variables for tracking target duration, cue, and feedback
    currentTargetDuration = startRT;
    feedbackImage = equalsImage;
    cueImage = incentiveCue;

    % Initialize Psychtoolbox
    PsychDefaultSetup(2);
    Screen('Preference', 'SkipSyncTests', 1);
    %Screen('Preference', 'VisualDebugLevel', 3);
    
    % Open a Window
    [wPtr, rect] = Screen('OpenWindow', screenNum, [], []);
    Screen('TextSize', wPtr, 40);
    Screen('TextFont', wPtr, 'Helvetica');
    % Set the blend function to handle transparency
    Screen('BlendFunction', wPtr, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    
    % Define trigger codes
    triggers = struct('beginExperiment', 100, 'ITI', 19, ...
                      'incentiveCue', 11, 'neutralCue', 10, ...
                      'targetOnset', 13, 'successfulKeypress', 14, 'otherKeypress', 15, ...
                      'thumbsUpFeedback', 16, 'equalSignFeedback', 17, 'endTask', 200);


    % Set max priority for better timing
    %Priority(MaxPriority(wPtr));

    % Set the escape key
    escapeKey = KbName('q');
    
    %CHECK FOR RTBOX
    RTBoxFound = checkForRTBox;

    Screen('FillRect', wPtr, [255 255 255]);
    DrawFormattedText(wPtr,'When you are ready press the SPACEBAR to begin the task.','center','center',[0,0,0]); % center on x and y coordinate
    Screen('Flip',wPtr);
    KbWait(-1);

    if RTBoxFound, RTBox('TTL', triggers.beginExperiment); end % Begin experiment trigger
    triggerTime = GetSecs();

        
    % Experiment Loop Begins ------------------------------------------------------------------
    for trial = 1:length(trialTypes)

        % zero out all keypress times each trial
        SKeyTime = 0;
        OKeyTime = 0;

        fprintf('\nTrial number: %d\t', trial);
        fprintf('Type: %s\t', trialTypes(trial));
        
        targetDuration(trial) = currentTargetDuration;
        fprintf('Current target duration: %f\t', currentTargetDuration);

        % Intertrial Interval
        Screen('FillRect', wPtr, [255 255 255]);
        Screen('Flip', wPtr);
        % Send ITI onset trigger
        if RTBoxFound, RTBox('TTL', triggers.ITI); end
        ITITime = GetSecs() - triggerTime;
        WaitSecs(ITIduration);

        % Listen for keypresses
        while (GetSecs() - ITITime) < ITIduration
            [keyIsPressed, secs, keyCode] = KbCheck;
            if keyIsPressed
                OKeyTime = secs - triggerTime;
            end
            if keyIsPressed && keyCode(escapeKey)
                break;
            end
        end

        Screen('FillRect', wPtr, [255 255 255]);
        if strcmp(trialTypes(trial), "incentive")
            cueImage(:, :, 4) = alphaI;
            cueImageTexture = Screen('MakeTexture', wPtr, cueImage);
        else
            neutralCue(:, :, 4) = alphaN;
            cueImageTexture = Screen('MakeTexture', wPtr, neutralCue);
        end
        Screen('DrawTexture', wPtr, cueImageTexture, [], [], 0);
        [~, cueOnsetTime] = Screen('Flip', wPtr);

        % Send cue presentation trigger
        if RTBoxFound, RTBox('TTL', triggers.(trialTypes(trial) + "Cue")); end
        if strcmp(trialTypes(trial), 'incentive')
            ICueTime = cueOnsetTime - triggerTime;
            NCueTime = 0;
        else
            ICueTime = 0;
            NCueTime = cueOnsetTime - triggerTime;
        end

        % WaitSecs(cueDuration);

        while (GetSecs() - cueOnsetTime) < cueDuration
            [keyIsPressed, secs, keyCode] = KbCheck;
            if keyIsPressed
                OKeyTime = secs - triggerTime;
            end
            if keyIsPressed && keyCode(escapeKey)
                break;
            end
        end
        if keyIsPressed && keyCode(escapeKey)
            break;
        end
        if keyIsPressed
            % Send other keypress trigger
            if RTBoxFound, RTBox('TTL', triggers.otherKeypress); end
            fprintf('cue keypress\t');
        end
        
        % Anticipation Period
        fixationDuration = rand() * (fixationMaxDuration - fixationMinDuration) + fixationMinDuration;
        antDuration(trial) = fixationDuration;
        Screen('FillRect', wPtr, [255 255 255]);
        TextRect = Screen('TextBounds',wPtr,'+');
        TextWidth = TextRect(3);
        TextHeight = TextRect(4);
        TextX = rect(3)/2-TextWidth/2;
        TextY = rect(4)/2-TextHeight/2;
        DrawFormattedText(wPtr, '+', TextX, TextY, [0 0 0]);
        [~, antOnTime] = Screen('Flip', wPtr);

        while (GetSecs() - antOnTime) < fixationDuration
            [keyIsPressed, secs, keyCode] = KbCheck(-1);
            if keyIsPressed
                OKeyTime = secs - triggerTime;
            end
            if keyIsPressed && keyCode(escapeKey)
                break;
            end
        end
        if keyIsPressed 
            % Send other keypress trigger
            if RTBoxFound, RTBox('TTL', triggers.otherKeypress); end
            fprintf('anticipation keypress\t');
        elseif keyIsPressed && keyCode(escapeKey)
            break;
        end
        
        % Target stimulus
        Screen('FillRect', wPtr, [255 255 255]);
        Screen('Flip', wPtr);
        targetImage(:, :, 4) = alphaT; % specify the alpha channel for the texture
        targetImageTexture = Screen('MakeTexture', wPtr, targetImage);
        Screen('DrawTexture', wPtr, targetImageTexture, [], [], 0);
        [~, targetOnsetTime] = Screen('Flip', wPtr);

        % Send target onset trigger
        if RTBoxFound, RTBox('TTL', triggers.targetOnset); end
        TargetOnTime = targetOnsetTime - triggerTime;

        % Listen for successful keypress
        while (GetSecs() - targetOnsetTime) < currentTargetDuration
            [successKey, secs, keyCode] = KbCheck(-1);
            if successKey
                if keyCode(KbName('Space'))
                    % if RTBoxFound, RTBox('TTL', triggers.successfulKeypress); end
                    RT(trial) = secs - targetOnsetTime;
                    status(trial) = 1;
                    SKeyTime = secs - triggerTime;
                    break;
                else
                    status(trial) = 0;
                    RT(trial) = 99;
                end
            else
                status(trial) = 0;
                RT(trial) = 99;
            end
            if (GetSecs() - targetOnsetTime) >= currentTargetDuration
                break;
            end
        end
        fprintf('status of trial %d: %d\t', trial, status(trial));
        % Send keypress trigger
        if status(trial) == 1
            if RTBoxFound, RTBox('TTL', triggers.successfulKeypress); end
            % This makes sure the target time does not drop below 50ms
            currentTargetDuration = max(currentTargetDuration - targetDurationChange, 0.05);
            fprintf('Successful Keypress!\t');
        else
            currentTargetDuration = currentTargetDuration + targetDurationChange;
        end
        
        % Fixation after target
        Screen('FillRect', wPtr, [255 255 255]);
        TextRect = Screen('TextBounds',wPtr,'+');
        TextWidth = TextRect(3);
        TextHeight = TextRect(4);
        TextX = rect(3)/2-TextWidth/2;
        TextY = rect(4)/2-TextHeight/2;
        DrawFormattedText(wPtr, '+', TextX, TextY, [0 0 0]);
        [~, fixAfterTargOnsetTime] = Screen('Flip', wPtr);

        while (GetSecs() - fixAfterTargOnsetTime) < fixationAfterTarget
            [keyIsPressed, secs, keyCode] = KbCheck;
            if keyIsPressed
                OKeyTime = secs - triggerTime;
            end
            if keyIsPressed && keyCode(escapeKey)
                break;
            end
        end
        if keyIsPressed && keyCode(escapeKey)
            break;
        elseif keyIsPressed
            % Send other keypress trigger
            if RTBoxFound, RTBox('TTL', triggers.otherKeypress); end
            fprintf('after target keypress\t');
        end
        
        % Feedback presentation
        Screen('FillRect', wPtr, [255 255 255]);
        if strcmp(trialTypes(trial), "incentive") && status(trial) == 1
            thumbsUpImage(:, :, 4) = alphaU;
            feedbackImageTexture = Screen('MakeTexture', wPtr, thumbsUpImage);
            % Send feedback trigger
            if RTBoxFound, RTBox('TTL', triggers.thumbsUpFeedback); end
            UpTime = GetSecs() - triggerTime;
            EqualsTime = 0;
        else
            feedbackImage(:, :, 4) = alphaE;
            feedbackImageTexture = Screen('MakeTexture', wPtr, feedbackImage);
            % Send feedback trigger
            if RTBoxFound, RTBox('TTL', triggers.equalSignFeedback); end
            UpTime = 0;
            EqualsTime = GetSecs() - triggerTime;
        end
        Screen('DrawTexture', wPtr, feedbackImageTexture, [], [], 0);
        [~, feedOnsetTime] = Screen('Flip', wPtr);
        WaitSecs(feedbackDuration);

        while (GetSecs() - feedOnsetTime) < feedbackDuration
            [keyIsPressed, secs, keyCode] = KbCheck;
            if keyIsPressed
                OKeyTime = secs - triggerTime;
            end
            if keyIsPressed && keyCode(escapeKey)
                break;
            end
        end
        if keyIsPressed && keyCode(escapeKey)
            break;
        end
        if keyIsPressed
            % Send other keypress trigger
            if RTBoxFound, RTBox('TTL', triggers.otherKeypress); end
            fprintf('feedback keypress\t');
        end
        
        % Clear textures
        Screen('Close', feedbackImageTexture);

        %Record trigger times in logfile for this trial
        fprintf(outfile,'%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\n',ICueTime, NCueTime, TargetOnTime, SKeyTime, OKeyTime, UpTime, EqualsTime, ITITime);

        if trial == length(trialTypes)
            fprintf('Next Round Start Target Duration = %f\n', currentTargetDuration)
        end
    end

    % End of experiment trigger
    if RTBoxFound, RTBox('TTL', triggers.endTask); end
    
    % Save data to CSV file using writematrix
    data = [trialNumber', trialTypes', antDuration', targetDuration', status', RT'];
    headers = {'Trial', 'TrialType', 'Anticipation', 'Target', 'Status', 'RT'};
    % Combine headers and data
    labeledData = [headers; num2cell(data)];

    writecell(labeledData, fullFilePath, 'Delimiter', ',', 'WriteMode', 'overwrite');

    fclose(outfile);

    Screen('FillRect', wPtr, [255 255 255]);
    DrawFormattedText(wPtr,'Good job, you have completed one round of the task!','center','center',[0,0,0]);
    Screen('Flip', wPtr);
    WaitSecs(3);
    %Priority(0);
    Screen('CloseAll');
    clear all;
    sca;
    return;
end