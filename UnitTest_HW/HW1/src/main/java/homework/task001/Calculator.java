package homework.task001;

public class Calculator {
    public static int calculation(int firstOperand, int secondOperand, char operator) {
        int result;

        switch (operator) {
            case '+' -> result = firstOperand + secondOperand;
            case '-' -> result = firstOperand - secondOperand;
            case '*' -> result = firstOperand * secondOperand;
            case '/' -> {
                if (secondOperand != 0) {
                    result = firstOperand / secondOperand;
                } else {
                    throw new ArithmeticException("Division by zero is not possible");
                }
            }
            default -> throw new IllegalStateException("Unexpected value operator: " + operator);
        }
        return result;
    }

    // HW1.1: Придумайте и опишите (можно в псевдокоде) функцию извлечения корня и
    // необходимые проверки для него используя граничные случаи
    public static double squareRootExtraction(double num) {
        //  0
        //  Отрицательные числа
        //  Дробные значения корней
        //  Целые
        if (num < 0) {
            throw new IllegalArgumentException("Cannot calculate square root of a negative number");
        }
        return Math.sqrt(num);
    }

    // Нужно написать в калькуляторе метод вычисления суммы покупки со скидкой и проверить его, используя AssertJ
    // Примерная сигнатура и тело метода:
    public static double calculatingDiscount(double purchaseAmount, int discountAmount) {
        // purchaseAmount - сумма покупки
        // discountAmount - размер скидки
        double resultAmount = purchaseAmount * (100 - discountAmount) / 100;
        if (purchaseAmount < 1)
            throw new IllegalArgumentException("Сумма покупок не может быть меньше 1 usd");
        if (discountAmount < 0) throw new IllegalArgumentException("Процент скидки не может быть отрицательным");
        if (resultAmount < 0) throw new IllegalArgumentException("Процент скидки не может быть больше 100");
        return resultAmount; // Метод должен возвращать сумму покупки со скидкой
    }
}
