local module = {}
mqtt = nil

local function send_message(message)
    -- Sends a simple ping to the broker
    mqtt:publish("/mcu2pi/", message, 0, 0 , function(client) 
        print("node2mcu succeed")
    end)
end

local function mqtt_start()
    -- initiate the mqtt client and set keepalive timer to 120sec
    mqtt = mqtt.Client(config.ID, 120, config.USERNAME, config.PASSWORD)
    --register message callback beforehand
    mqtt:on("message", function(client, topic, data)
        if data ~= nil then
            print(topic .. ": " .. data)
            --consume_data(payload)
            --do something with the payload and send responce
            --match
            --print(string.find(data, config.USERNAME))
            if string.find(data, config.USERNAME) ~= nil
            then
                --do something if payload contain device name
                if string.find(data, "on") ~= nil
                then
                    gpio.mode(config.DEVICE,gpio.OUTPUT)
                    gpio.write(config.DEVICE,gpio.HIGH)
                    send_message(config.USERNAME .. "on")
                elseif string.find(data, "off") ~= nil
                then
                    gpio.mode(config.DEVICE,gpio.OUTPUT)
                    gpio.write(config.DEVICE, gpio.LOW)
                    send_message(config.USERNAME .. "off")
                else
                    print("gpio setting error!")
                end                
            end
        end
    end)
    -- Connect to broker
    mqtt:connect(config.HOST, config.PORT, 0, 1, function(client)
        --register_myself()
        -- Sends my id to the broker for registration
        mqtt:subscribe("/pi2mcu/",0,function(client)
            -- subscribe topic pi2mcu
            print("Successfully subscribed to PI2MCU")
            --send_message()
        end)
    end)
end

function module.start()
    mqtt_start()
end

return module
