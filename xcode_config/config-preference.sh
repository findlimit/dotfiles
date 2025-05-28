#!/bin/sh
#
# Xcode specific settings

echo "- Setting up Xcode"

# Trim trailing whitespace
defaults write com.apple.dt.Xcode DVTTextEditorTrimTrailingWhitespace -bool true

# Trim whitespace only lines
defaults write com.apple.dt.Xcode DVTTextEditorTrimWhitespaceOnlyLines -bool true

# Show invisible characters
defaults write com.apple.dt.Xcode DVTTextShowInvisibleCharacters -bool true

# Show line numbers
defaults write com.apple.dt.Xcode DVTTextShowLineNumbers -bool true

# Set key binding mode to Vi
defaults write com.apple.dt.Xcode DVTTextEditorKeyBindings -string "Vi"

# Set custom keybindings preference to VSCode.idekeybindings
cp ./VSCode.idekeybindings ~/Library/Developer/Xcode/UserData/KeyBindings/
defaults write com.apple.dt.Xcode IDEKeyBindingCurrentPreferenceSet -string "VSCode.idekeybindings"
