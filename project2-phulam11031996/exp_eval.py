from array_stack import empty_stack, push, pop, is_empty, peek


# str -> float
def postfix_eval(input_string: str) -> float:
    """Evaluates the given RPN expression.

    Args:
        input_string: an RPN expression

    Returns:
        The result of the expression evaluation

    Raises:
        ValueError: if the input is not well-formed
        ZeroDivisionError: if the input would cause division by zero
    """
    validate_input(input_string)

    postfix = input_string.split()
    eval_stack = empty_stack()
    arr_len = len(postfix)

    for i in range(0, arr_len):
        if postfix[i] not in ('+', '-', '*', '/', '//', '**', '^'):
            push(eval_stack, float(postfix[i]))
        elif postfix[i] == '+':
            second = pop(eval_stack)
            first = pop(eval_stack)

            push(eval_stack, first + second)

        elif postfix[i] == '-':
            second = pop(eval_stack)
            first = pop(eval_stack)

            push(eval_stack, first - second)

        elif postfix[i] == '*':
            second = pop(eval_stack)
            first = pop(eval_stack)

            push(eval_stack, first * second)

        elif postfix[i] == '/':
            second = pop(eval_stack)
            first = pop(eval_stack)
            try:
                push(eval_stack, first / second)
            except ZeroDivisionError:
                raise ZeroDivisionError

        elif postfix[i] == '**' or postfix[i] == '^':
            second = pop(eval_stack)
            first = pop(eval_stack)

            push(eval_stack, pow(first, second))

        elif postfix[i] == '//':
            second = pop(eval_stack)
            first = pop(eval_stack)

            push(eval_stack, first // second)

    return pop(eval_stack)


# str -> no return values
def validate_input(input_string: str):
    """Validates input_string

    Args:
        input_string: an infix expression

    Returns:
        no return values
    """

    if len(input_string) == 0:  # empty input
        raise ValueError('empty input')

    operator_counter = 0    # insufficent or too many operands
    operand_counter = 0
    for input in input_string.split():
        if input in ['+', '-', '*', '/', '//', '**', '^']:
            operator_counter += 1
        else:
            operand_counter += 1

    if (operand_counter - 1) > operator_counter:
        raise ValueError('too many operands')

    if (operand_counter - 1) < operator_counter:
        raise ValueError('insufficient operands')

    for input in input_string.split():
        if input not in ['+', '-', '*', '/', '//', '**', '^']:
            try:
                float(input)
            except ValueError:
                raise ValueError('invalid token')


# str -> str
def infix_to_postfix(input_string: str) -> str:
    """Converts the given infix string to RPN.

    Args:
        input_string: an infix expression

    Returns:
        The equivalent expression in RPN
    """

    rpn = empty_stack()
    stack = empty_stack()
    operators = ['+', '-', '*', '/', '//', '**', '^']

    for input in input_string.split():
        if input not in operators and input not in ['(', ')']:
            push(rpn, input)
        elif input == '(':
            push(stack, input)
        elif input == ')':
            while peek(stack) != '(':
                push(rpn, pop(stack))

            pop(stack)
        else:
            while (not is_empty(stack) and
                    (peek(stack) in operators) and
                    ((op_pre(peek(stack)) > op_pre(input)) or
                   (op_pre(peek(stack)) == op_pre(input) != 3))):

                push(rpn, pop(stack))
            push(stack, input)

    while not is_empty(stack):
        push(rpn, pop(stack))

    new_rpn = []
    idx = 0
    for idx in range(rpn.size):
        new_rpn.append(rpn.items[idx])
        idx += 1

    return ' '.join(new_rpn)


# str -> int
def op_pre(oper: str) -> int:
    """Calulate the oper's precedence

    Args:
        oper: oper in string type

    Returns:
        precedence: precedence of oper in int
    """
    if oper == '+' or oper == '-':
        return 1
    elif oper == '*' or oper == '/' or oper == '//':
        return 2
    else:
        return 3
