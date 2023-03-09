use super::*;

fn part1(grid: &Array2D<i32>) -> String{
    let goal = (grid.num_rows() - 1, grid.num_columns() - 1);
    let result = astar(&(0,0), |p| neighbours(grid, *p, false).into_iter().map(|p| (p, grid[p])),
    |&(x, y)| (goal.0.abs_diff(x) as i32 + goal.1.abs_diff(y) as i32),
    |&p| p == goal);
    result.expect("no path found").1.to_string()
}

fn part2(grid: &Array2D<i32>) -> String{
    let goal = (grid.num_rows() * 5 - 1, grid.num_columns() * 5 - 1);
    let result = astar(&(0,0), |p| neighbours_from_size(&(grid.num_rows() * 5, grid.num_columns() * 5), *p, false).into_iter().map(|p| (p, part2_cost(grid, &p))),
    |&(x, y)| (goal.0.abs_diff(x) as i32 + goal.1.abs_diff(y) as i32),
    |&p| p == goal);
    result.expect("no path found").1.to_string()
}

fn part2_cost(grid: &Array2D<i32>, point: &(usize, usize)) -> i32{
    let p = (point.0 % (grid.num_rows()),
                        point.1 % (grid.num_columns()));
    let add = (point.0 / grid.num_rows())
                    + point.1 / grid.num_columns();
    ((grid[p] as usize + add - 1) % 9 + 1) as i32
}


pub(crate) fn solve(input: &str) -> (String, String){
    let grid = to_grid(input).unwrap_or(Array2D::filled_with(0, 1, 1));
    (part1(&grid), part2(&grid))
}