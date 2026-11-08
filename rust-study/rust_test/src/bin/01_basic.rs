fn main(){//프로그램 진입점

    println!("Hello, World!");

    //변(Immutable) 변수 선언
    let language= "Rust";
    println!("Hello, {}", language);

    //가변(Mutable) 변수 선언
    let mut day_count = 1;
    println!("Day: {}", day_count);

    day_count += 1;
    println!("Day: {}", day_count);
}