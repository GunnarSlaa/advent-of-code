use array2d::Array2D;

pub(crate) fn neighbours(grid: &Array2D<i32>, (row, col): (usize, usize)) -> Vec<(usize, usize)>{
    let mut neighbours = Vec::new();
    if row > 0 {neighbours.push((row - 1, col))}
    if col > 0 {neighbours.push((row, col - 1))}
    if col < (grid.num_columns() - 1)  {neighbours.push((row, col + 1))}
    if row < (grid.num_rows() - 1)  {neighbours.push((row + 1, col))}
    neighbours
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_neighbours() {
        let grid = Array2D::filled_with(0, 3, 3);
        assert_eq!(neighbours(&grid, (0, 0)).len(), 2);
        assert_eq!(neighbours(&grid, (1, 1)).len(), 4);
        assert_eq!(neighbours(&grid, (2, 1)).len(), 3);
        let grid2 = Array2D::filled_with(0, 5, 3);
        assert_eq!(neighbours(&grid2, (0, 0)).len(), 2);
        assert_eq!(neighbours(&grid2, (4, 2)).len(), 2);
        assert_eq!(neighbours(&grid2, (4, 2)), vec![(3, 2), (4, 1)]);
        assert_eq!(neighbours(&grid2, (4, 1)).len(), 3);
    }
}