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

    // HW1.1: ���������� � ������� (����� � ����������) ������� ���������� ����� �
    // ����������� �������� ��� ���� ��������� ��������� ������
    public static double squareRootExtraction(double num) {
        //  0
        //  ������������� �����
        //  ������� �������� ������
        //  �����
        if (num < 0) {
            throw new IllegalArgumentException("Cannot calculate square root of a negative number");
        }
        return Math.sqrt(num);
    }

    // ����� �������� � ������������ ����� ���������� ����� ������� �� ������� � ��������� ���, ��������� AssertJ
    // ��������� ��������� � ���� ������:
    public static double calculatingDiscount(double purchaseAmount, int discountAmount) {
        // purchaseAmount - ����� �������
        // discountAmount - ������ ������
        double resultAmount = purchaseAmount * (100 - discountAmount) / 100;
        if (purchaseAmount < 1)
            throw new IllegalArgumentException("����� ������� �� ����� ���� ������ 1 usd");
        if (discountAmount < 0) throw new IllegalArgumentException("������� ������ �� ����� ���� �������������");
        if (resultAmount < 0) throw new IllegalArgumentException("������� ������ �� ����� ���� ������ 100");
        return resultAmount; // ����� ������ ���������� ����� ������� �� �������
    }
}
