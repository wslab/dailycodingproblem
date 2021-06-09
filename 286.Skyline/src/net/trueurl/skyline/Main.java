package net.trueurl.skyline;

import java.util.ArrayList;
import java.util.List;

/*
This problem was asked by VMware.

The skyline of a city is composed of several buildings of various widths and heights,
possibly overlapping one another when viewed from a distance. We can represent the buildings
using an array of (left, right, height) tuples, which tell us where on an imaginary x-axis
a building begins and ends, and how tall it is. The skyline itself can be described by
a list of (x, height) tuples, giving the locations at which the height visible to
a distant observer changes, and each new height.

Given an array of buildings as described above, create a function that returns the skyline.

For example, suppose the input consists of the buildings [(0, 15, 3), (4, 11, 5), (19, 23, 4)].
In aggregate, these buildings would create a skyline that looks like the one below.

     ______
    |      |        ___
 ___|      |___    |   |
|   |   B  |   |   | C |
| A |      | A |   |   |
|   |      |   |   |   |
------------------------
As a result, your function should return [(0, 3), (4, 5), (11, 3), (15, 0), (19, 4), (23, 0)]
 */
public class Main {
    // height of skyline at the point "coord"
    public static int skylineAt(double coord, House[] houses) {
        int current = 0;
        for (House house : houses)
            if (house.heightAt(coord) > current) current = house.heightAt(coord);
        return current;
    }

    // next start or end of building
    public static int nextChange(int coord, House[] houses) {
        int result = Integer.MAX_VALUE;
        for (House house : houses) {
            if (house.left > coord && house.left < result) {
                result = house.left;
                continue;
            }
            if (house.right > coord && house.right < result) {
                result = house.right;
            }
        }
        return result;
    }

    public static List<int[]> solve(House[] houses) {
        // assume houses are already sorted by left coordinate
        // House[] sorted_houses = sortHouses(houses);
        House[] sorted_houses = houses;
        List<int[]> result = new ArrayList<int[]>();
        int start = sorted_houses[0].left;
        result.add(new int[]{start, skylineAt(start, sorted_houses)});
        int nextChangeCoord = nextChange(start, sorted_houses);
        while (nextChangeCoord < Integer.MAX_VALUE) {
            int nextNext = nextChange(nextChangeCoord, houses);
            if (nextNext == Integer.MAX_VALUE) {
                result.add(new int[]{nextChangeCoord, 0});
            } else {
                result.add(new int[]{nextChangeCoord, skylineAt((nextChangeCoord + nextNext) / 2.0, sorted_houses)});
            }
            nextChangeCoord = nextChange(nextChangeCoord, sorted_houses);
        }
        return result;
    }

    public static String res2str(int[] res) {
        return "[" + res[0] + "," + res[1] + "]";
    }

    public static void main(String[] args) {
        //[(0, 15, 3), (4, 11, 5), (19, 23, 4)]
        House[] houses = new House[]{
                new House(0, 15, 3),
                new House(4, 11, 5),
                new House(19, 23, 4)};
        List<int[]> result = solve(houses);
        for (int[] r : result) System.out.println(res2str(r));
    }

}
