package net.trueurl.skyline;

public class House {
    int left;
    int right;
    int height;

    public House(int left, int right, int height) {
        this.left = left;
        this.right = right;
        this.height = height;
    }

    int heightAt(double coord) {
        if (coord >= this.left && coord <= this.right)
            return this.height;
        else return 0;
    }

}
