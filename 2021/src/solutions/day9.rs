use array2d::Array2D;
use help::grid::neighbours;
use help::parsing::to_grid;

fn low_points(grid: &Array2D<i32>) -> Vec<(usize, usize)>{
    let mut points = Vec::new();
    for col in 0..grid.num_columns(){
        'cell: for row in 0..grid.num_rows(){
            for nb in neighbours(grid, (row, col)){
                if grid[nb] <= grid[(row, col)] {continue 'cell;}
            }
            points.push((row, col));
        }
    }
    points
}

fn part1(grid: &Array2D<i32>) -> i32{
    low_points(grid).iter().map(|x| grid[*x] + 1).sum()
}

fn part2(grid: &Array2D<i32>) -> i32{
    0
}

pub(crate) fn solve(input: &str) -> (String, String){
    let grid = to_grid(input).unwrap_or(Array2D::filled_with(0, 1, 1));
    println!("num_columns: {}", grid.num_columns());
    println!("num_rows: {}", grid.num_rows());
    (part1(&grid).to_string(), part2(&grid).to_string())
}