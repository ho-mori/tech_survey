import { sum } from "../src/sum";

// write a test for sum
describe("sum", () => {
  it("should return the sum of two numbers", () => {
    expect(sum(1, 2)).toBe(3);
    expect(sum(-1, -1)).toBe(-2);
    expect(sum(0, 0)).toBe(0);
    expect(sum(1.5, 2.5)).toBe(4);
  });
});
