package homework;

import org.junit.jupiter.api.Test;
import static org.assertj.core.api.Assertions.assertThat;


class VehicleTest {

    Car car = new Car("Toyota", "RAV4", 2018);
    Motorcycle moto = new Motorcycle("Baltmotors", "Galactica", 2022);

    //- проверяем, что экземпляр объекта Car также является экземпляром транспортного средства; (instanceof)
    @Test
    void instanceOf() {
        //Car car = new Car("Toyota", "RAV4", 2018);
        assertThat(car instanceof Vehicle);
    }

    //- проверяем, что объект Car создается с 4-мя колесами
    @Test
    void WheelsCar() {
        //Car car = new Car("Toyota", "RAV4", 2018);
        assertThat(car.getNumWheels()).isEqualTo(4);
    }

    // - проверяем, что объект Motorcycle создается с 2-мя колесами
    @Test
    void MotorcycleWheels() {
        //Motorcycle moto = new Motorcycle("Baltmotors", "Galactica", 2022);
        assertThat(moto.getNumWheels()).isEqualTo(2);
    }

    //- проверяем, что объект Car развивает скорость 60 в режиме тестового вождения (testDrive())
    @Test
    void testDriveCar() {
        car.testDrive();
        assertThat(car.getSpeed()).isEqualTo(60);
    }

    // - проверяем, что объект Motorcycle развивает скорость 75 в режиме тестового вождения (testDrive())
    @Test
    void testDriveMotorcycle() {
        moto.testDrive();
        assertThat(moto.getSpeed()).isEqualTo(75);
    }

    //- проверяем, что в режиме парковки (сначала testDrive, потом park,
    // т.е эмуляция движения транспорта) машина останавливается (speed = 0)
    @Test
    void parkCar() {
        car.testDrive();
        //System.out.println(car.getSpeed());
        car.park();
        assertThat(car.getSpeed()).isEqualTo(0);
    }

    //- проверяем, что в режиме парковки (сначала testDrive, потом park
    // т.е эмуляция движения транспорта) мотоцикл останавливается (speed = 0)
    @Test
    void parkMotorcycle() {
        moto.testDrive();
        //System.out.println(moto.getSpeed());
        moto.park();
        assertThat(moto.getSpeed()).isEqualTo(0);
    }

}

