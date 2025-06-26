package Paradigmas.Java;

import java.util.List;

public class Entregavel1 {
    public static void main(String[] args) {
        List<Integer> numbers = List.of(10, 9, 8, 7, 6, 5, 4, 3, 2, 1);
        System.out.println("Lista Original: " + numbers);
        
        System.out.println("\nFiltra pares:");
        filter(numbers);
        System.out.println("\nMultiplica por 2:");
        transform(numbers);
        System.out.println("\nOrdena crescente:");
        order(numbers);
        System.out.println("\nLinha a Linha:");
        print(numbers);
    }

    private static void filter(List<Integer> numbers){
        System.out.println(numbers.stream().filter(x -> x % 2 == 0).toList());
    }

    private static void transform(List<Integer> numbers){
        System.out.println(numbers.stream().map(x -> x * 2).toList());
    }

    private static void order(List<Integer> numbers){
        System.out.println(numbers.stream().sorted().toList());
    }

    private static void print(List<Integer> numbers){
        numbers.forEach(x -> System.out.println(x));
    }
}