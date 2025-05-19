import { describe, it, expect } from "vitest";
import { add } from "./math";

describe("add", () => {
  it("1 + 2 = 3", () => {
    expect(add(1, 2)).toBe(3);
  });
});
