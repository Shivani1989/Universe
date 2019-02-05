class checksumCal{
private val sum=0
def sum(b:byte):Unit ={
sum+=b
}
def checksum():Int={
return ~(sum & 0xFF)+1
}
}
