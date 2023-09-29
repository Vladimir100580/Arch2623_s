package Classes;

import Enumerators.TypeCar;
import Enumerators.TypeFuel;
import Enumerators.TypeGearBox;
import Interfaces.ICarWash;
import Interfaces.IFuelStation;
import Interfaces.IStreetCleanup;

import java.awt.*;

public class SpecialRoadCleaner extends Car implements IFuelStation, ICarWash, IStreetCleanup {

    private int waterCap;

    public SpecialRoadCleaner(String make, String model,
                              int numberWheels, TypeFuel fuelType, TypeGearBox gearBoxType,
                              Color bodyColor, int engineCap) {

        super(make, model, TypeCar.SPECIAL_ROAD_CLEANER, numberWheels, fuelType, gearBoxType, bodyColor, engineCap);
    }

    @Override
    public void wipWindshield() {

    }

    @Override
    public void wipHeadlights() {

    }

    @Override
    public void wipMirrors() {

    }

    @Override
    public void fuel() {

    }

    @Override
    public void sweepStreet() {

    }
}
