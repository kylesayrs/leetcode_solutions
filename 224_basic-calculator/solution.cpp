#include<string>
#include <exception>

enum Op { minus_u, minus_b, plus, null };


class Solution {
public:
    void newVal(
        int new_value,
        int &a,
        int &a_null,
        int &b,
        int &b_null
    ) {
        if (a_null) {
            a = new_value;
            a_null = false;
        } else {
            b = new_value;
            b_null = false;
        }
    }

    int eval(int &index) {
        // initialize state
        int a = 0;
        int a_null = true;
        int b = 0;
        int b_null = true;
        Op op = Op::null;

        while (true) {
            // blanks do nothing
            if (str[index] == ' ') {
                
            
            // recurse on open parens
            } else if (str[index] == '(') {
                index += 1;
                newVal(eval(index), a, a_null, b, b_null);

            // return on close parens or string end
            } else if (str[index] == ')' || index >= str.size()) {
                assert(!a_null);
                assert(b_null);
                assert(op == Op::null);
                return a;
            
            // handle digits
            } else if (str[index] >= '0' && str[index] <= '9') {
                int new_val = static_cast<int>(str[index] - '0');

                // attempt to append, otherwise store value
                if (!b_null) {
                    assert(op != Op::null);  // must have seen an operator before assigning to b
                    b = b * 10 + new_val;
                } else if (!a_null && op == Op::null) {
                    a = a * 10 + new_val;
                } else {
                    newVal(new_val, a, a_null, b, b_null);
                }
            
            // minus can be unary or binary
            } else if (str[index] == '-') {
                if (a_null) {
                    op = Op::minus_u;
                
                } else {
                    op = Op::minus_b;
                }
            
            // plus is only binary
            } else if (str[index] == '+') {
                op = Op::plus;
            
            // unhandled character
            } else {
                throw std::invalid_argument("unknown character");
            }

            // evaluate if next char is not number
            if (index + 1 >= str.size() || str[index + 1] < '0' || str[index + 1] > '9') {
                if (op == Op::minus_u && !a_null) {
                    a = -a;
                    op = Op::null;
                
                } else if (op == Op::minus_b && !b_null) {
                    assert(!a_null);
                    a = a - b;
                    b_null = true;
                    op = Op::null;
                
                } else if (op == Op::plus && !b_null) {
                    assert(!a_null);
                    a = a + b;
                    b_null = true;
                    op = Op::null;
                }
            }

            // increment index
            index += 1;

        }
    }

    int calculate(std::string s) {
        str = s;

        int index = 0;
        return this->eval(index);
    }

    std::string str;
};


int main() {
    Solution solution;
    assert(solution.calculate("1 + 2") == 3);
    assert(solution.calculate("1 + 2 + 3") == 6);
    assert(solution.calculate("1 + 2 - 3") == 0);
    assert(solution.calculate("1 - 2 + 3") == 2);
    assert(solution.calculate("- 2 + 3") == 1);
    assert(solution.calculate("- (2 + 3)") == -5);
    assert(solution.calculate("- (2 + (3))") == -5);
    assert(solution.calculate("11 + 22") == 33);
    assert(solution.calculate("11 + 22333333") == 11 + 22333333);
    assert(solution.calculate("11 + 22333333") == 11 + 22333333);
}
