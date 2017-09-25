package expression;

import java.util.Stack;

public class FPExpression extends Expression {

    /**
     * Constructor for FPExpression. This is a private constructor. Objects of
     * this type can only be created by clients through a call to the static
     * method 'getFPExpression(String)' or 'getFPExpression(Expression)'. This
     * is to preserve the representation invariant and the sub-typing
     * relationship.
     * 
     * @param expression
     */
    private FPExpression(String expression) {
        super(expression);
    }

    /**
     * 
     * @param expression
     * @return an FPExpression object with the same input expression if the
     *         input expression is fully parenthesized.
     * @throws IllegalArgumentException
     *             if the input is not a valid fully parenthesized expression.
     */
    public static FPExpression getFPExpression(String expression) throws IllegalArgumentException {
        if (!isFPExpression(expression)) {
            throw new IllegalArgumentException();
        }
        // If the input String is a valid fully parenthesized expression then
        // the following statement is correct.
        // This uses the private constructor.
        return new FPExpression(expression);

    }

    /**
     * 
     * @param expression
     * @return an FPExpression object with the input expression string if the
     *         input expression is fully parenthesized.
     * @throws IllegalArgumentException
     *             if the input is not a valid fully parenthesized expression.
     */
    public static FPExpression getFPExpression(Expression expression) throws IllegalArgumentException {
        if (!isFPExpression(expression.toString())) {
            throw new IllegalArgumentException();
        }
        // If the input String is a valid fully parenthesized expression then
        // the following statement is correct.
        // This uses the private constructor.
        return new FPExpression(expression.toString());

    }

    /**
     * Given an Expression, check if the expression is a fully parenthesized
     * expression.
     * 
     * @param expression
     * @return true if expression is fully parenthesized and false otherwise
     */
    public static boolean isFPExpression(Expression expression) {
        // This method is okay. Don't have to change this.
        return isFPExpression(expression.toString());
    }

    /**
     * Given a String check if the string represents a fully parenthesized
     * expression.
     * 
     * @param expression
     * @return true if expression is fully parenthesized and false otherwise
     */
    public static boolean isFPExpression(String expression) {
        // IFP : is fully parenthesized
        boolean IFP = true;
        if (expression == null || expression == "") {
            IFP = false;
        } else {
            Stack<Character> brackets = new Stack<>();
            char[] expArray = expression.toCharArray();
            boolean emptyStack = true;

            for (int index = 0; index < expArray.length; index++) {
                char nextChar = expArray[index];
                if (nextChar == '(' || nextChar == '[' || nextChar == '{') {
                    brackets.push(nextChar);
                } else {
                    emptyStack = brackets.isEmpty();
                    if (nextChar == ')') {
                        if (emptyStack) {
                            IFP = false;
                            break;
                        } else if (brackets.pop() != '(') {
                            IFP = false;
                            break;
                        }

                    } else if (nextChar == ']') {
                        if (emptyStack) {
                            IFP = false;
                            break;
                        } else if (brackets.pop() != '[') {
                            IFP = false;
                            break;
                        }

                    } else if (nextChar == '}') {
                        if (emptyStack) {
                            IFP = false;
                            break;
                        } else if (brackets.pop() != '{') {
                            IFP = false;
                            break;
                        }

                    }
                }
            }
            if (!brackets.isEmpty()) {
                IFP = false;
            }
        }
        return IFP;
    }

}
