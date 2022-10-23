SLASH_DICT1 = '/dict';
SLASH_DICT2 = '/d';
function SlashCmdList.DICT(msg, editBox)
    term = msg
        :lower()
        :gsub('à', 'a')
        :gsub('è', 'e')
        :gsub('ì', 'i')
        :gsub('ò', 'o')
        :gsub('ù', 'u')
        :gsub('ç', 'c')
        :gsub('é', 'e')
        :gsub('â', 'a')
        :gsub('ê', 'e')
        :gsub('î', 'i')
        :gsub('ô', 'o')
        :gsub('û', 'u')
        :gsub('ë', 'e')
        :gsub('ï', 'i')
        :gsub('ü', 'u');
    
    word = words[term];
    if word == nil then
        print("No definitions found for " .. msg)
        return
    end

    print("Definitions for " .. msg .. ":")
    for i, line in ipairs(word) do
        print(i .. ". " .. line)
    end
end