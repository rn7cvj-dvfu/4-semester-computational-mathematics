from sympy import  lambdify, symbols , diff, Interval  , cos 
from sympy.calculus.util import maximum, minimum

from constants import A , B , STEPS_COUNT , PRECISION  , FUNCTION, CHECK_POINTS
from utils import getNearestPoints , Point , dividedDifference2 , dividedDifference3
 
x, psi = symbols("x psi")

h = (B - A) / STEPS_COUNT
print(f"H = {h}")
step_values : list[float] = [round(A + h * i , PRECISION) for i in range(STEPS_COUNT + 1)]


print('---------------------------------------------------')
for value in step_values:

    print(f"f({value}) = {FUNCTION(value)}")

print('---------------------------------------------------')

for point in CHECK_POINTS: 
    
    nearestPoints : list[Point] = getNearestPoints(step_values , point , h)

    previous , current , next = nearestPoints


    L1 = (FUNCTION(current.value) * (point - next.value ) / (current.value - next.value)) + (
        FUNCTION(next.value) * (point - current.value) / (next.value  -  current.value))
    

    FUNCTION_DIFF_2 =  diff(FUNCTION(x), x, 2)

    fd_2_min = minimum(FUNCTION_DIFF_2, x, Interval(current.value, next.value))
    fd_2_max = maximum(FUNCTION_DIFF_2, x, Interval(current.value, next.value))


    OMEGA_2_FUNCTION = (x - current.value) * (x - next.value)

    omega_2_min = minimum(OMEGA_2_FUNCTION, x, Interval(current.value, next.value))
    omega_2_max = maximum(OMEGA_2_FUNCTION, x, Interval(current.value, next.value))
    
    r1_min = fd_2_min * omega_2_min / 2
    r1_max = fd_2_max * omega_2_max / 2

    r1_value = FUNCTION(point) -  L1 

    if not(r1_min < r1_value and r1_value < r1_max):
        print(f"R1({point}) = {r1_value} isn`t in the interval [{r1_min} , {r1_max}]")

    L2  = (
        (
            (FUNCTION(previous.value) * (point - current.value) * (point- next.value)) /
            ((previous.value - current.value) * (previous.value - next.value))
        ) + 
        (
            (FUNCTION(current.value) * (point - previous.value) * (point - next.value)) /
            ((current.value - previous.value) * (current.value - next.value))
        ) + 
        (
            (FUNCTION(next.value) * (point - previous.value) * (point - current.value)) /
            ((next.value - previous.value) * (next.value - current.value))
        )
    )


    FUNCTION_DIFF_3 = diff(FUNCTION(x), x, 3)

    fd_3_min = minimum(FUNCTION_DIFF_3, x, Interval(previous.value, next.value))
    fd_3_max = maximum(FUNCTION_DIFF_3, x, Interval(previous.value, next.value))


    OMEGA_3_FUNCTION = (x - previous.value) * (x - current.value) * (x - next.value)

    omega_3_min = minimum(OMEGA_3_FUNCTION, x, Interval(previous.value, next.value))
    omega_3_max = maximum(OMEGA_3_FUNCTION, x, Interval(previous.value, next.value))

    r2_min = fd_3_min * omega_3_min  / 6
    r2_max = fd_3_max * omega_3_max  / 6

    r2_value = L2 - FUNCTION(point)  


    if not(r2_min < r2_value and r2_value < r2_max):
        print(f"R2({point}) = {r2_value} isn`t in the interval [{r2_min} , {r2_max}]")

    L1_NEWTON = FUNCTION(current.value)  + dividedDifference2(current.value , next.value , FUNCTION)  * (point - current.value)

    L2_NEWTON = FUNCTION(previous.value) + (
         dividedDifference2(previous.value , current.value , FUNCTION)  * (point - previous.value))  + (
             
                dividedDifference3(previous.value , current.value , next.value , FUNCTION) * (point - previous.value) * (point - current.value)

         )
       
    print("Calculating the value of the function at the point ", point)



    print(f"R1MIN {r1_min} , R1MAX {r1_max} | R1 {r1_value} | diff: {abs(r1_value - (r1_min + r1_max) / 2)}")
    print(f"R2MIN {r2_min} , R2MAX {r2_max} | R2 {r2_value} | diff: {abs(r2_value - (r2_min + r2_max) / 2)}")

    print()

    print(f"F(x): {FUNCTION(point)}")

    print()    

    print(f"L1 {L1} , L1_NEWTON {L1_NEWTON} | diff: {abs(L1 - L1_NEWTON)}")
    print(f"L2 {L2} , L2_NEWTON {L2_NEWTON} | diff: {abs(L2 - L2_NEWTON)}")

    print()

    print(f"diff L1 - F(X) : {abs(L1 - FUNCTION(point))}")
    print(f"diff L2 - F(X) : {abs(L2 - FUNCTION(point))}")

    print("---------------------------------------------------")

