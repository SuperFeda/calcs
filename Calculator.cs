class Calculator{
    public static void Main(string[] args) {
        Console.WriteLine("Enter first number >> ");
        double a = double.Parse(Console.ReadLine());
        Console.WriteLine("Enter second number >> ");
        double b = double.Parse(Console.ReadLine());
        Console.WriteLine("Enter operation (+ - * / **) >> ");
        string operation = Console.ReadLine();

        switch (operation) {
            case "+":
                Console.WriteLine($"{a} + {b} = {a + b}");
                break;
            case "-":
                Console.WriteLine($"{a} - {b} = {a - b}");
                break;
            case "*":
                Console.WriteLine($"{a} * {b} = {a * b}");
                break;
            case "/":
                if (b == 0) {
                    Console.WriteLine("Cannot divide by zero!");
                } else {
                    Console.WriteLine($"{a} / {b} = {a / b}");
                }
                break;
            case "**":
                Console.WriteLine($"{a} ** {b} = {Exponentiation(a, b)}");
                break;
            default:
                Console.WriteLine("Unknown operation!");
                break;
        }
    }

    private static double Exponentiation(double a, double b) {
        double result = 1;
        for (int i = 0; i < b; i++) { result = a * result; }
        return result;
    }
}