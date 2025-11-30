public class FourQueens {
    static final int N = 4;
    public static void main(String[] args) {
        int[][] board = new int[N][N];
        solveQueens(board, 0);
    }
    // Recursive function to place queens row by row
    static void solveQueens(int[][] board, int row) {
        // Base case: All queens are placed
        if (row == N) {
            printBoard(board);
            System.out.println();
            return;
        }
        // Try placing queen in each column of current row
        for (int col = 0; col < N; col++) {
            if (isSafe(board, row, col)) {
                board[row][col] = 1;      // place queen
                solveQueens(board, row + 1);  // recurse for next row
                board[row][col] = 0;      // backtrack
            }
        }
    }
    // Check if it's safe to place a queen at board[row][col]
    static boolean isSafe(int[][] board, int row, int col) {

        // Check this column in previous rows
        for (int i = 0; i < row; i++)
            if (board[i][col] == 1)
                return false;

        // Check upper-left diagonal
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--)
            if (board[i][j] == 1)
                return false;

        // Check upper-right diagonal
        for (int i = row - 1, j = col + 1; i >= 0 && j < N; i--, j++)
            if (board[i][j] == 1)
                return false;

        return true;
    }
    // Utility method to print the board
    static void printBoard(int[][] board) {
        for (int[] row : board) {
            for (int cell : row) {
                System.out.print(cell == 1 ? "Q " : ". ");
            }
            System.out.println();
        }
    }
}
