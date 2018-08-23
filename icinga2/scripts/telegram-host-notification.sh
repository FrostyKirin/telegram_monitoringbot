ELEGRAM_CHAT_ID=
TELEGRAM_BOT_TOKEN=

ICINGA_HOSTNAME="192.168.1.2"

#Set the message icon based on ICINGA service state
if [ "$HOSTSTATE" = "DOWN" ]
then
	    ICON="❌"
    elif [ "$HOSTSTATE" = "UP" ]
    then
	        ICON="✅"
	else
		    ICON="❓"
	    fi

	    template=$(cat <<TEMPLATE
	    ${ICON} ${NOTIFICATIONTYPE} - *${HOSTDISPLAYNAME}* - ${HOSTDISPLAYNAME} is *${HOSTSTATE}*
	    TEMPLATE
	    )

	    # Informations supplémentaires qui peuvent être affichées (réfléchir aux données sensibles (IP, adresses web))
	    # ${HOSTOUTPUT}
	    # [see more...](https://${ICINGA_HOSTNAME}/icingaweb2/monitoring/host/services?host=${HOSTNAME})

	    /usr/bin/curl --silent --output /dev/null \
		        --data-urlencode "chat_id=$TELEGRAM_CHAT_ID" \
			    --data-urlencode "text=${template}" \
			        --data-urlencode "parse_mode=Markdown" \
				    --data-urlencode "disable_web_page_preview=true" \
				        "https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage"


