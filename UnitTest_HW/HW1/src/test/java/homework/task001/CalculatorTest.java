package homework.task001;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

public class CalculatorTest {
    public static void main(String[] args) {
        // �������� �������� ����������� � ������ �������:
        if (8 != Calculator.calculation(2, 6, '+')) {
            throw new AssertionError("������ � ������");
        }

        if (0 != Calculator.calculation(2, 2, '-')) {
            throw new AssertionError("������ � ������");
        }

        if (14 != Calculator.calculation(2, 7, '*')) {
            throw new AssertionError("������ � ������");
        }

        if (2 != Calculator.calculation(100, 50, '/')) {
            throw new AssertionError("������ � ������");
        }

        // ������ � ������������� �����������
        // �������� operator ���� char, ������ �������� ����������, ���� �� �������� �� ������� ������� (+-*/)
        // try {
        //     seminars.first.Calculator.Calculator.calculation(8, 4, '_');
        // } catch (IllegalStateException e) {
        //     if (!e.getMessage().equals("Unexpected value operator: _")) {
        //         throw new AssertionError("������ � ������");
        //     }
        // }

        // �������� �������� ����������� � ������ �������, � �������������� �����������:
        assert 8 == Calculator.calculation(2, 6, '+');
        assert 0 == Calculator.calculation(2, 2, '-');
        assert 14 == Calculator.calculation(2, 7, '*');
        assert 2 == Calculator.calculation(100, 50, '/');

        // �������� �������� ����������� � ������ �������, � �������������� ����������� AssertJ:
//        assertThat(Calculator.calculation(2, 6, '+')).isEqualTo(8);
//        assertThat(Calculator.calculation(2, 2, '-')).isEqualTo(0);
//        assertThat(Calculator.calculation(2, 7, '*')).isEqualTo(14);
//        assertThat(Calculator.calculation(100, 50, '/')).isEqualTo(2);

        // �������� ���������� ����������, � �������������� ����������� AssertJ:
//        assertThatThrownBy(() ->
//                Calculator.calculation(8, 4, '_')
//        ).isInstanceOf(IllegalStateException.class);

        System.out.println(Calculator.calculation(2_147_483_647, 1, '+')); // integer overflow
        System.out.println(Calculator.squareRootExtraction(169));

        // ��������� ������� �������� ������� �� 1 ������:

        // HW1.1: ���������� � ������� (����� � ����������) ������� ���������� ����� �
        // ����������� �������� ��� ���� ��������� ��������� ������
        // assertThatThrownBy(() ->
        //         seminars.first.Calculator.Calculator.squareRootExtraction(0, 1, -1)
        // ).isInstanceOf(SomeStateException.class);

        // HW1.2: ��� ����� ��������� �������� ��� ������ ������� �� ����? (� �������������� AssertJ)
        // assertThatThrownBy(() ->
        //        seminars.first.Calculator.Calculator.calculation(5, 0, '/')
        // ).isInstanceOf(ArithmeticException.class);

        // HW1.3: �������� ���� � �� �� �������� � �������������� �������, ��������, AssertJ
        // � ����� ������ ����������� ��������� �� ������ ����� ����� �������������?
        // if (0 != seminars.first.Calculator.Calculator.calculation(2, 6, '+')) {
        //     throw new AssertionError("������ � ������");
        // }
        //   assert 0 == seminars.first.Calculator.Calculator.calculation(2, 6, '+');
        //    assertThat(seminars.first.Calculator.Calculator.calculation(2, 6, '+')).isEqualTo(0);
    }

    /**
     * ���������� ����� ������� ������ �����
     */
    @Test
    public void purchaseAmountCannotLessOne() {
        String messageException = "����� ������� �� ����� ���� ������ 1 usd";
        Exception exception = assertThrows(IllegalArgumentException.class, () ->
                Calculator.calculatingDiscount(0, 10));
        assertEquals(messageException, exception.getMessage());
    }

    /**
     * ���������� ������� ������ ������ ����
     */
    @Test
    public void discountAmountCannotLessZero() {
        String message = "������� ������ �� ����� ���� �������������";
        Exception exception = assertThrows(IllegalArgumentException.class, () ->
                Calculator.calculatingDiscount(100, -5));
        assertEquals(message, exception.getMessage());
    }

    /**
     * ���������� ������� ������ ������ 100
     */
    @Test
    public void discountAmountCannotMoreHundred() {
        String message1 = "������� ������ �� ����� ���� ������ 100";
        Exception exception = assertThrows(IllegalArgumentException.class, () ->
                Calculator.calculatingDiscount(100, 115));
        assertEquals(message1, exception.getMessage());
    }
}


