code = """
x = 10
y = 20
print(x+y)
"""

compiled = compile(code, "<string>", "exec")

exec(compiled)

print(eval("10+20"))