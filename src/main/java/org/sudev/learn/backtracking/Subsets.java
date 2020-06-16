package org.sudev.learn.backtracking;

import java.util.ArrayList;

/**
 * InterviewBit - https://www.interviewbit.com/problems/subset/
 * @author sudev.ac on 22/05/20
 */
public class Subsets {

    private static ArrayList<Integer> removeAnElement(ArrayList<Integer> arr, Integer pos) {
        ArrayList<Integer> newArray = new ArrayList<>();
        for (int i = 0; i < arr.size(); i++) {
            if (i != pos) {
                newArray.add(arr.get(i));
            }
        }
        return newArray;
    }

    private static ArrayList<ArrayList<Integer>> loop(ArrayList<Integer> arr, ArrayList<ArrayList<Integer>> accum) {
        for (int pos = 0; pos < arr.size(); pos++) {
            // Constrains
            ArrayList<Integer> newSet = removeAnElement(arr, pos);
            if (!accum.contains(newSet)) accum.add(newSet);
            loop(removeAnElement(arr, pos), accum);
        }
        return accum;
    }

    public static ArrayList<ArrayList<Integer>> subsets(ArrayList<Integer> A) {
        ArrayList<ArrayList<Integer>> solutions = new ArrayList<>();
        solutions.add(A);
        return loop(A, solutions);
    }

    public static void main(String[] args) {
        ArrayList<Integer> integers = new ArrayList<>();
        integers.add(1);
        integers.add(2);
        integers.add(3);
        subsets(integers);
        System.out.println(subsets(integers));
    }
}
