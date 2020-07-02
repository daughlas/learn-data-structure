public class Main {

    public static void main(String[] args) {

        Array<Integer> arr = new Array<>(20);
        for(int i = 0 ; i < 10 ; i ++)
            arr.addLast(i);
        System.out.println(arr);

        arr.add(1, 100);
        System.out.println(arr);

        arr.addFirst(-1);
        System.out.println(arr);
        // [-1, 0, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        arr.remove(2);
        System.out.println(arr);

        arr.removeElement(4);
        System.out.println(arr);

        arr.removeFirst();
        System.out.println(arr);

        Array<Student> students = new Array<>();
        students.addLast(new Student("a", 10));
        students.addLast(new Student("b", 20));
        students.addLast(new Student("c", 30));

        System.out.println(students);
    }
}
