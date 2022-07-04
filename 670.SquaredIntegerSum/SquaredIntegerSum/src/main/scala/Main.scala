object Main extends App {

  def generateSquares(limit: Int): Seq[Int] = {
    if (limit <0 ) Seq()
    else {
      val aaa = Stream.from(1).map(x=>x*x).takeWhile(x => x <= limit)
      // convert stream to seq
      Seq[Int]() ++ aaa
    }
  }

  def attempt(targetSum: Int, pieces: Seq[Int], currentCount: Int): Int = {
    println(s"targetSum: $targetSum, currentCount: $currentCount")
    if (targetSum == 0) currentCount
    else {
//      val goodPieces = pieces.filter(x => x <= targetSum)
//      val processedPieces = goodPieces.map(x => attempt(targetSum-x, pieces, currentCount+1))
//      val res = processedPieces.min
//      res
      pieces
        .filter(x => x <= targetSum)
        .map(x => attempt(targetSum-x, pieces, currentCount+1)).min
    }
  }

  def solve(targetSum: Int): Int = {
    if (targetSum <=0 ) 0
    else {
      val squares = generateSquares(targetSum).reverse
      attempt(targetSum, squares, 0)
    }
  }

  generateSquares(27)
  val res = solve(27)
  println(s"res = $res")

}
