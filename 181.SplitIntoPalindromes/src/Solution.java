/*
This problem was asked by Google.

Given a string, split it into as few strings as possible such that each string is a palindrome.

For example, given the input string racecarannakayak, return ["racecar", "anna", "kayak"].

Given the input string abc, return ["a", "b", "c"]

 */


import java.util.ArrayList;
import java.util.List;

public class Solution {

    public static boolean isPalindrome(String s, int startIndex, int endIndex) {
        String candidate = s.substring(startIndex, endIndex);
        return isPalindrome(candidate);
    }

    public static boolean isPalindrome(String s) {
        char[] chars = s.toCharArray();
        if ( chars.length < 2 ) return true;
        int beginIdx = 0;
        int endIdx = chars.length - 1;
        while (beginIdx < endIdx ) {
            if (chars[beginIdx] != chars[endIdx]) return false;
            beginIdx += 1;
            endIdx -= 1;
        }
        return true;
    }

    public static List<String> solve(String s) {
        List<String> res = new ArrayList<String>();
        return solve2(s, res);
    }

    public static List<String> solve2(String s, List<String> res) {
        if ( s.isEmpty() ) return res;
        int len = firstPalindromeLength(s);
        String firstPalindrome = s.substring(0, len);
        res.add(firstPalindrome);
        String rest = s.substring(len);
        return solve2(rest, res);
    }

    public static int firstPalindromeLength(String s) {
        for (int i = s.length(); i > 0; i--) {
            if (isPalindrome(s, 0, i)) return i;
        }
        return 1;
    }

    public static void printList(List<String> list) {
        System.out.println(String.join(",", list));
    }

    public static void main(String[] args) {
        System.out.println("main");
        System.out.println(isPalindrome("aba"));
        System.out.println(isPalindrome("abccba"));
        System.out.println(isPalindrome("haha"));
        System.out.println(firstPalindromeLength("racecarannakayak"));
        System.out.println(firstPalindromeLength("abc"));
        printList(solve("racecarannakayak"));
        printList(solve("abc"));
        printList(solve("abcracecarannakayak"));
        printList(solve("racecarannakayakabc"));
    }
}
