--<include file not found>
p = primary --> static
secondary = {}

function secondary:new(o)
    o = o or {}

    setmetatable(o, self)
    self.__index = self
    return o
end

s = secondary --> static
