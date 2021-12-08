def insertion_sort(liste):
    for i in range(1, len(liste)):
        aktuellerWert = liste[i]
        aktuellePosition = i
        while aktuellePosition > 0 and liste[aktuellePosition - 1] > aktuellerWert:
            liste[aktuellePosition] = liste[aktuellePosition - 1]
            aktuellePosition  = aktuellePosition -1

        liste[aktuellePosition] = aktuellerWert

def insertion_sort_copy(liste):

    l2 = liste.copy()

    for i in range(1, len(l2)):
        aktuellerWert = l2[i]
        aktuellePosition = i
        while aktuellePosition > 0 and l2[aktuellePosition - 1] > aktuellerWert:
            liste[aktuellePosition] = l2[aktuellePosition - 1]
            aktuellePosition  = aktuellePosition -1

        liste[aktuellePosition] = aktuellerWert
    
    return l2


def bubble_sort(liste):
    weitermachen = True
    while weitermachen:
        weitermachen = False
        for i in range(0, len(liste)-1):
            if liste[i] > liste[i+1]:
                # wechsle i und i+1 um
                liste[i], liste[i+1] = liste[i+1], liste[i]
                weitermachen = True

# schlimmster Fall: O(n*n)      # O-Notation

# merge sort O(n * log n)

l = [5,3,2,8,10,1,0]
#bubble_sort(l)

l2 = sorted(l) # neue Liste

print(l)
print(l2)

neueliste = [6,4,3,8,6,3,6,8]
neueliste.sort()
print(neueliste)


neueliste = [6,4,3,8,6,3,6,8]
neueliste.sort(reverse=True)
print(neueliste)



