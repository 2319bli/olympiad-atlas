CREATE TABLE `account_papers` (
	`user_id` text NOT NULL,
	`paper_id` text NOT NULL,
	`payload` text NOT NULL,
	`created_at` integer NOT NULL,
	PRIMARY KEY(`user_id`, `paper_id`)
);
--> statement-breakpoint
CREATE TABLE `account_progress` (
	`user_id` text NOT NULL,
	`problem_id` text NOT NULL,
	`saved` integer NOT NULL,
	`status` text NOT NULL,
	`updated_at` integer NOT NULL,
	PRIMARY KEY(`user_id`, `problem_id`)
);
