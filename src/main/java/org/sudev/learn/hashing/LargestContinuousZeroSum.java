package org.sudev.learn.hashing;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.ToString;
import lombok.var;

import java.util.*;
import java.util.stream.Collectors;

import static java.util.Arrays.asList;

/**
 * @author sudev.ac on 31/05/20
 */
public class LargestContinuousZeroSum {
    private List<Integer> array;

    public LargestContinuousZeroSum(List<Integer> array) {
        this.array = array;
    }

    public static void main(String[] args) {
        ArrayList<Integer> integers = new ArrayList<>(asList(-19, 8, 2, -8, 19, 5, -2, -23));
        ArrayList<Integer> integers1 = new ArrayList<>(asList(1, 2, -2, 4, -4));
        ArrayList<Integer> integers2 = new ArrayList<>(asList(1, 2, -3, 3));
        LargestContinuousZeroSum largestContinuousZeroSum = new LargestContinuousZeroSum(integers1);
        largestContinuousZeroSum.solve();

        // Leet code solve

        /*largestContinuousZeroSum.lszero(integers);*/
        /*System.out.println(lszeroOptimal(integers));*/
        /*System.out.println(lszeroOptimal(integers1));*/
        System.out.println(lszeroOptimal(integers2));
    }

    // Solution - optimal solution using hash
    public static ArrayList<Integer> lszeroOptimal(ArrayList<Integer> A) {
        if (A.isEmpty()) {
            return A;
        }
        HashMap<Integer, List<Integer>> sums = new HashMap<>();
        int tempSum = 0;
        for (int i = 0; i < A.size(); i++) {
            tempSum = A.get(i) + tempSum;
            if (sums.containsKey(tempSum)) {
                List<Integer> integers = sums.get(tempSum);
                integers.add(i);
            } else {
                sums.put(tempSum, new ArrayList<>(Collections.singletonList(i)));
            }
        }
        int start = -1;
        int end = -1;
        int size = 0;
        for (Map.Entry<Integer, List<Integer>> sum : sums.entrySet()) {
            int tempStart = Collections.min(sum.getValue());
            int tempEnd = Collections.max(sum.getValue());
            int tempSize = tempEnd - tempStart;
            if ((tempSize > size) || ((tempSize == size) && (tempStart < start))) {
                start = tempStart;
                end = tempEnd;
                size = tempSize;
            }

        }
        ArrayList<Integer> result = new ArrayList<>();
        for (int i = start + 1; i < end; i++) {
            result.add(A.get(i));
        }
        return result;
    }

    public Solution solve() {
        List<Solution> solutionList = new ArrayList<>();
        for (int i = 0; i < array.size(); i++) {
            var sum = 0;
            for (int j = i; j < array.size(); j++) {
                Integer elem = this.array.get(j);
                sum = sum + elem;
                if (sum == 0) {
                    Solution solution = new Solution(j - i + 1, i, j);
                    solutionList.add(solution);
                }
            }
        }
        //System.out.println(solutionList);
        //solutionList.forEach(this::print);
        Solution solution = solutionList.stream().max(Comparator.comparingInt(Solution::getSize)).get();
        print(solution);
        return solution;
    }

    public void print(Solution solution) {
        List<Integer> temp = new ArrayList();
        for (int i = solution.getStart(); i <= solution.getEnd(); i++) {
            temp.add(this.array.get(i));
        }
        String collect = temp.stream().map(String::valueOf).collect(Collectors.joining(" "));
        System.out.println(solution);
        System.out.println(collect);
    }

    // Solution - first without using memory
    public ArrayList<Integer> lszero(ArrayList<Integer> A) {
        int size = -1;
        int start = -1;
        int end = -1;
        for (int i = 0; i < A.size(); i++) {
            int sum = 0;
            for (int j = i; j < A.size(); j++) {
                int elem = A.get(j);
                sum = sum + elem;
                if (sum == 0) {
                    int newSize = j - i + 1;
                    if (newSize > size) {
                        start = i;
                        end = j;
                        size = newSize;
                    }
                }
            }
        }
        ArrayList<Integer> temp = new ArrayList();
        if (size == -1) {
            return temp;
        } else {
            for (int i = start; i <= end; i++) {
                temp.add(A.get(i));
            }
            return temp;
        }
    }

    @Getter
    @AllArgsConstructor
    @ToString
    static class Solution {
        Integer size;
        Integer start;
        Integer end;
    }
}
