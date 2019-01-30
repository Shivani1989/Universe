import scala.collection.mutable
import scala.collection.immutable

val treasureMap= mutable.Map[Int, String]()
treasureMap+=(1->"Go to island")
treasureMap+=(2->"Find happiness")
treasureMap+=(3->"Relax & Enjoy")
println(treasureMap(2))

val romanval = immutable.Map[Int, String](1->"I", 2->"II", 3->"III")
//romanval+=(4->"IV") - Error cz immutable
println(romanval(2))
