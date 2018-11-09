#!/bin/sh
 
UNITY_EXECUTABLE="/Applications/Unity/Unity.app/Contents/MacOS/Unity"
PROJECT_FOLDER="/Users/findlimit/FourDesire/plantnanny2-client"
RESULTS_FILENAME="PNT.Test.Result.xml"
TESTNAME="PNT.Test.Test_PNTCorDataManager.DataProperties_BeforeAgentSet_ThrowNullRefereceException"
 
echo "Run Unity.app (in batch mode) with editor test..."
 
time \
"$UNITY_EXECUTABLE" \
-batchmode \
-nographics \
-projectPath "$PROJECT_FOLDER" \
-runEditorTests \
-editorTestsResults "$PROJECT_FOLDER/$RESULTS_FILENAME" \
-editorTestsFilter "$TESTNAME" \
