import java.util.Scanner;

public class Calc {
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.print("Enter first num >> ");
        double num1 = scanner.nextDouble();

        System.out.print("Enter second num >> ");
        double num2 = scanner.nextDouble();

        System.out.print("Enter operation (+, -, *, /, **) >> ");
        String operation = scanner.next();

        switch (operation) {
            case "+":
                System.out.printf("%f + %f = " + (num1 + num2) + "\n", num1, num2);
                break;
            case "-":
                System.out.printf("%f - %f = " + (num1 - num2) + "\n", num1, num2);
                break;
            case "**":
                System.out.printf("%f ** %f = " + exponent(num1, num2) + "\n", num1, num2);
                break;
            case "*":
                System.out.printf("%f * %f = " + (num1 * num2) + "\n", num1, num2);
                break;
            case "/":
                if (num2 != 0) {
                    System.out.printf("%f / %f = " + (num1 / num2) + "\n", num1, num2);
                } else {
                    System.out.println("Error. Zero Division.");
                }
                break;
            default:
                System.out.printf("Error. Operation \"%s\" is not current.\n", operation);
                break;
        }

        scanner.close();
    }

    private static double exponent(double num1, double num2) {
        double result = 1;

        for (int i = 0; i < (int)num2; i++) {
            result = num1 * result;
        }

        return result;
    }
}