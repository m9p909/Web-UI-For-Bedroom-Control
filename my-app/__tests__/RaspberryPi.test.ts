//Author: Jack Clarke
import RaspberryPi from "../lib/RaspberryPi";
const PI_IP_ADDRESS = "http://localhost";
const PI_PORT = 808;
test("set and get port", () => {
  const pi = new RaspberryPi("ipaddress", 1234);
  expect(pi.getPort()).toBe(1234);
  pi.setPort(4567);
  expect(pi.getPort()).toBe(4567);
});

test("make sure calls are defined", () => {
  const pi = new RaspberryPi(PI_IP_ADDRESS, PI_PORT);
  if (pi.isUp()) {
    expect(pi.getHumidity()).toBeDefined();
    expect(pi.getLight()).toBeDefined();
    expect(pi.getTemp()).toBeDefined();
    expect(pi.doorOpen()).toBeDefined();
  }
});
