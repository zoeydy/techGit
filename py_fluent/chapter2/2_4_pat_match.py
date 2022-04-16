""" Pattern Matching with Sequences """

# e.g.2-9 Destructuring nested tuples—requires Python ≥ 3.10.
# TODO:不知道为什么总是显示语法不合理或者indentation error，暂时放一放
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

def main():
    print(f'{"":15},{"latitude":>9},{"longitude":>9}')
    for record in metro_areas:
        match record:
            case [name, _, _, (lat, lon)] if lon <= 0:
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')






# E.g. 2-10 Matching patterns without match/case.
def evaluate(x, env):
    "evaluate an expression in an environment"
    if ...: # several lines omitted
        ...
    elif x[0] == 'quote': # (quote exp)
        (_, exp) = x
        return exp
    elif x[0] == 'if': # (if test conseq alt)
        (_, test, conseq, alt) = x
        exp = (conseq if evaluate(test, env) else alt)
        return evaluate(exp, env)
    elif x[0] == 'define': # (define var exp)
        (_, var, exp) = x
        env[var] = evaluate(exp, env)
    elif x[0] == 'lambda': # (lambda (var ...) boy ...)
        (_, parms, *body) = x
        return Procedure(parms, body, env)
    # more lines omitted


# TODO: 省略号的问题
# E.g. 2-11 Pattern matching with match/case—requires Python ≥ 3.10
# def evaluate(exp, env):
#     "Evaluate an expression in an environment." 
#     match exp:
#         case ...: # several lines omitted 
#             ...
#         case ['quote', exp]: 
#             return exp
#         case ['if', test, conseq, alt]:
#             exp = (conseq if evaluate(test, env) else alt) 
#             return evaluate(exp, env)
#         case ['define', Symbol(var), exp]:
#             env[var] = evaluate(exp, env)
#         case ['lambda', parms, *body] if len(body) >= 1: 
#             return Procedure(parms, body, env)
#         # more lines omitted
#         case _:
#             raise SyntaxError(repr(exp))