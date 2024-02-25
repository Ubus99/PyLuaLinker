s = require("secondary") --> static

primary = {}

function primary:new(o)
    o = o or {}

    self.s = s:new()

    setmetatable(o, self)
    self.__index = self
    return o
end