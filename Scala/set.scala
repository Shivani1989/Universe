
import scala.collection.mutable

var s= Set(1,2,3)
s+=4
println(s.contains(2))

val movieSet= mutable.Set("DDLJ", "HRJPK")
movieSet+="HAHK"
println(movieSet)

import scala.collection.immutable.HashSet

val hashSet= HashSet("A", "B")
//hashSet+='C' -- throws error cz set is immutable
println(hashSet+"C")
