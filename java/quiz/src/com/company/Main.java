package com.company;


import java.util.Random;
import java.util.Scanner;

public class Main {


//        数当てゲーム
        public static void main(String args[]){
            Random rnd = new Random();
            int question = rnd.nextInt(101);
            int limit = 10;

            Scanner sc = new Scanner(System.in);
            System.out.println("数当てゲームです。数字を入力してください");
            System.out.println("回答回数は" + limit + "回までです");

            for (int i = 0; i < limit; i++) {
                int answer = sc.nextInt();
                if (answer == question) {
                    System.out.println("正解です");
                    break;
                } else if (answer > question) {
                    System.out.println("それよりも下です");
                } else {
                    System.out.println("それよりも上です");
                }
            }
            System.out.println("正解は" + question + "でした");

        }
    }






