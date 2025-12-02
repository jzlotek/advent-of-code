fn part1(input: &Vec<&str>) -> i32 {
    let mut count = 0;
    let mut pos = 50;

    for line in input {
        let mut iter = line.chars();
        let mult = match iter.next() {
            Some(c) => {
                match c {
                    'L' => -1,
                    _ => 1,
                }
            }
            // dont care. this isnt production
            _ => 1
        };
        let val = iter.as_str().parse::<i32>().unwrap();
        pos += val * mult;
        pos = pos.rem_euclid(100);
        println!("{}", pos);
        count += i32::from(pos == 0);
    }

    count
}

fn part2(input: &Vec<&str>) -> i32 {
    let mut count = 0;
    let mut pos = 50;

    for line in input {
        let mut iter = line.chars();
        let mult = match iter.next() {
            Some(c) => {
                match c {
                    'L' => -1,
                    _ => 1,
                }
            }
            // dont care. this isnt production
            _ => 1
        };

        let val = iter.as_str().parse::<i32>().unwrap();
        let prev = pos;
        pos += val * mult;
        pos = pos.rem_euclid(100);

        if pos != 0 && prev != 0 && ((prev > pos && mult == 1) || (prev < pos && mult == -1)) {
            count += 1;
        }

        let additional = val / 100;
        count += additional + i32::from(pos == 0);
    }

    count
}
pub fn run() {
    let input: Vec<&str> = include_str!("./day_01.txt")
        .lines()
        .map(|x| x.trim())
        .collect();

    println!("1.a: {:?}", part1(&input));
    println!("1.b: {:?}", part2(&input));
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_p1() {
        let input: Vec<&str> = vec![
            "L68",
            "L30",
            "R48",
            "L5",
            "R60",
            "L55",
            "L1",
            "L99",
            "R14",
            "L82",
        ];
        assert_eq!(part1(&input), 3);
    }
    #[test]
    fn test_p2() {
        let input: Vec<&str> = vec![
            "L68",
            "L30",
            "R48",
            "L5",
            "R60",
            "L55",
            "L1",
            "L99",
            "R14",
            "L82",
        ];
        assert_eq!(part2(&input), 6);
    }
}
