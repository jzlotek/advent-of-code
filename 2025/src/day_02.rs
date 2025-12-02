
fn is_invalid(string: &str) -> bool {
    let length = string.len();
    if length % 2 == 1{
        return false;
    }
    let splits = string.split_at(length / 2);
    splits.0 == splits.1
}

fn is_invalid_seq(string: &str) -> bool {
    let mut length = string.len() / 2;

    while length > 0 {
        if string.len() % length != 0 {
            length -= 1;
            continue
        }
        let mut iter = string.as_bytes().chunks(length);
        let base = iter.next().unwrap();
        if iter
            .filter(|&x| x == base)
            .collect::<Vec<_>>()
            .len() == (string.len() / length - 1) {
                return true
        }

        length -= 1;
    }

    false
}

fn part1(input: &Vec<(u64, u64)>) -> u64 {
    input.iter().copied().map(
        |(x, y)| {
            let mut count = 0;
            for i in x..=y {
                if is_invalid(i.to_string().as_str()) {
                    count += i; 
                }
            }
            count
        }
    ).sum()
}

fn part2(input: &Vec<(u64, u64)>) -> u64 {
    input.iter().copied().map(
        |(x, y)| {
            let mut count = 0;
            for i in x..=y {
                if is_invalid_seq(i.to_string().as_str()) {
                    count += i; 
                }
            }
            count
        }
    ).sum()
}

pub fn run() {
    let input = parse_input(include_str!("./day_02.txt"));

    println!("2.a: {:?}", part1(&input));
    println!("2.b: {:?}", part2(&input));
}

fn parse_input(input: &str) -> Vec<(u64, u64)> {
            input.trim().split(",")
            .map(|x| x.split_once("-").unwrap())
            .map(|(x, y)| (x.parse().unwrap(), y.parse().unwrap()))
            .collect()
}


#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_p1() {
        let input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124";
        assert_eq!(part1(&parse_input(&input)), 1227775554);
    }
    #[test]
    fn test_p2() {
        let input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124";
        assert_eq!(part2(&parse_input(&input)), 4174379265);
    }
}
