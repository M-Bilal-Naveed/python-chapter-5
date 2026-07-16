a={
    "bilal": 100,
    "usama": 85,
    "abdullah": 75,
}

#items()
# give us the key value pairs form data the data that its gave us in tuple form

print(a.items())

#keys()
#give us the keys all in a dirt

print(a.keys())

#values()
#give us the values in a dirt

print(a.values())

#update()
# use to update the value of a thing inside the dirt using the key

a.update({"bilal":90})
print(a)

a.update({"bilal":90, "taimoor":88})
print(a)
#also add the new values in a dirt

#get()
#get method use to get the value using its key
print(a.get("bilal"))
