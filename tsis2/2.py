# https://leetcode.com/problems/goal-parser-interpretation/submissions/
class Solution:
    def interpret(self, command: str) -> str:
        command = command.replace("()", "o")
        return(command.replace("(al)", "al"))