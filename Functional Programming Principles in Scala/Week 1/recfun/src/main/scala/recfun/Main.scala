package recfun
import common._
import scala.annotation.tailrec
import scala.collection.mutable.ListBuffer

object Main {
  def main(args: Array[String]) {
    println("Pascal's Triangle")
    for (row <- 0 to 10) {
      for (col <- 0 to row)
        print(pascal(col, row) + " ")
      println()
    }
    println("Exercise 2")
    println(balance("()".toList))
    println(balance("())".toList))
  }

  /**
   * Exercise 1
   */
  def pascal(c: Int, r: Int): Int = {
    if (c <= 0 || c >= r) 1
    else pascal(c, r - 1) + pascal(c - 1, r - 1)
  }

  /**
   * Exercise 2
   */
  def balance(chars: List[Char]): Boolean = {
    @tailrec
    def balanced(chars: List[Char], open: Int): Boolean =
      chars match {
        case Nil => open == 0
        case '(' :: t => balanced(t, open + 1)
        case ')' :: t => open > 0 && balanced(t, open - 1)
        case _ :: t => balanced(t, open)
      }

    balanced(chars, 0)
  }

  /**
   * Exercise 3
   */
  def countChange(money: Int, coins: List[Int]): Int = {
    def f(lastMaxCoin_total_coll: List[(Int, Int)], count: Int): Int = {
      if (lastMaxCoin_total_coll.isEmpty) {
        count
      } else {
        val b = ListBuffer[(Int, Int)]()
        var newCount = count
        for ((lastMaxCoin, total) <- lastMaxCoin_total_coll) {
          if (total < money) {
            for (c <- coins) {
              if (c >= lastMaxCoin) {
                val e = (c, total + c)
                b += e
              }
            }
          } else if (total == money) {
            newCount += 1
          }
        }

        f(b.toList, newCount)
      }
    }

    val b = coins.map { c => (c, c) }
    f(b, 0)
  }
}
