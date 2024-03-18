package coding;
import java.util.*;
import java.io.*;

public class test {
    public static void main(String[] args) {
        // 문자열 배열을 List로 변환
        String[] temp = {"abcde", "asdf"};
        List<String> list = new ArrayList<>(Arrays.asList(temp));

// List를 문자열 배열로 변환
        List<String> list1 = new ArrayList<>();
        String[] temp1 = list.toArray(new String[list1.size()]);

// 정수 배열을 List로 변환
        int[] temp2 = { 1123, 1412, 23, 44, 512132 };
        List<int []> list2 = Arrays.asList(temp2);

// List를 정수 배열로 변환
        List<Integer> list3 = new ArrayList<>();
        int[] temp3 = list3.stream().mapToInt(i->i).toArray();
    }
}
