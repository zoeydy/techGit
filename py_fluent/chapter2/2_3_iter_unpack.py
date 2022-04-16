

lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates # unpacking
latitude
longitude

a = 3
b = 7
a, b = b, a
a
b


t = (20, 8)
divmod(20, 8) == divmod(*t)
quotient, remainder = divmod(*t)
quotient
remainder


import os
os.getcwd()
# os.chdir(os.getcwd())
cwd = os.getcwd()
os.path.split(cwd)
_, file_name = os.path.split(f'{cwd},/2_3_iter_unpack.py')
file_name


# Using * to grab excess items
a, b, *rest = range(5)
a,b,rest
a, b, *rest = range(3)
a,b,rest
a, b, *rest = range(2)
a,b,rest

a, *body, c, d = range(5)
a, body, c, d
*head, b, c, d = range(5) 
head, b, c, d

def fun(a,b,c,d,*rest):
    print(f"{a}_{b}_{c}_{d}_{rest}")
    return a,b,c,d,rest
fun(*[1, 2], 3, 'other', *range(6, 9))
fun(*[1,2],3,*range(6,9))

*range(4), 4
[*range(4), 4]
{*range(4), 4, *(5, 6, 7)}


# nested unpacking
# e.g.2-8 Unpacking nested tuples to access the longitude
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for name,_,_,(lat,lon) in metro_areas:
        if lon<0:
            print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')

if __name__ == "__main__":
    main()

