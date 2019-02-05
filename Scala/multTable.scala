def rowSeq(num:Int) = {
for (col <- 1 to 10) yield {
  val prod = (col*num).toString
  val padding = ' '*(4-prod.length)
  padding+prod
}
}

def rowSeqString(num: Int)= rowSeq(num).mkString

def multTable() = {
val tableSeq = for (row<- 1 to 10)
yield rowSeqString(row)
println(tableSeq.mkString("\n"))

}
