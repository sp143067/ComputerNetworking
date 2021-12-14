#!/usr/bin/expect

set timeout 10

spawn nc berlioz.cs.unh.edu 25


expect "220" {
	send "EHLO agate.cs.unh.edu\n"
	expect "250" {
		send "mail from: this_expect_test@fake.edu\n"
		expect "250" {
			send "rcpt to: sp1430@wildcats.unh.edu\n"
			expect "250" {
				send "data\n"
				expect "354" {
					send "From: this_expect_test@fake.edu\n"
					send "Content-Type: text/plain;\n"
					send "Subject: Assignment-3 SMTP Test Email\n"
					send "Date: Fri, 24 Oct 2020\n"
					send "To: Sandeep Kumar Paul <sp143@wildcats.unh.edu>\n\n"
					send "Hello CS825,\n\n"
					send "Hope you are well!\n"
					send "This is a netcat & expect test email. \n\n"
					send "Regards,\n"
					send "Sandeep Kumar Paul.\n"
					send "This email was sent on 24th October,2020.\n"
					send "\n.\n"
					expect "250" {
						send "quit\n"
					}
				}
			}
		}
	}
}
